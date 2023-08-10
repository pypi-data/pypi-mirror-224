import os
import sys
from datetime import datetime
from functools import cache
from itertools import chain
from os import path

import click
from more_itertools import quantify

from .constants import SHADER_DIRS
from .helpers import resolve_shader_path
from .hyprctl import clear_screen_shader, get_screen_shader, set_screen_shader
from .utils import systemd_user_config_home


@click.group()
def cli():
    pass


def main():
    try:
        cli()
    except Exception as e:
        click.echo(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


@cli.command()
@click.argument("shader_name_or_path")
def on(shader_name_or_path: str):
    """Turn on screen shader."""

    shader_path = resolve_shader_path(shader_name_or_path)
    set_screen_shader(shader_path)


@cli.command()
def off():
    """Turn off screen shader."""

    clear_screen_shader()


def is_same_shader(s: str | None, s2: str | None) -> bool:
    if s is None or s2 is None:
        return False
    s, s2 = resolve_shader_path(s), resolve_shader_path(s2)
    return path.samefile(s, s2)


@cli.command()
@click.argument("shader_name_or_path", default=None)
@click.option(
    "--fallback",
    metavar="SHADER",
    help="Shader to switch to instead of toggling off.",
)
@click.option(
    "--fallback-default",
    is_flag=True,
    default=False,
    help="Use default shader as fallback. (see --fallback)",
)
@click.option(
    "--fallback-auto",
    is_flag=True,
    default=False,
    help="Use currently scheduled shader as fallback."
    " (If the currently scheduled shader is SHADER_NAME_OR_PATH, the default"
    " shader will be used as the fallback instead.)",
)
@click.pass_context
def toggle(
    ctx: click.Context,
    shader_name_or_path: str | None,
    fallback: str | None,
    fallback_default: bool,
    fallback_auto: bool,
):
    """Toggle screen shader.

    If run with no arguments, SHADER_NAME_OR_PATH is inferred based on schedule.

    When --fallback is specified, will toggle between SHADER_NAME_OR_PATH and the
    fallback shader. --fallback-default will toggle between SHADER_NAME_OR_PATH and the
    default shader, whereas --fallback-auto will toggle between SHADER_NAME_OR_PATH and
    the currently scheduled shader. (--fallback-auto is equivalent to --fallback-default
    if the currently scheduled shader is SHADER_NAME_OR_PATH.)
    """

    from .config import Schedule

    @cache
    def schedule() -> Schedule:
        from .config import Config

        return Config().to_schedule()

    fallback_opts = [fallback, fallback_default, fallback_auto]
    if quantify(fallback_opts) > 1:
        raise click.BadOptionUsage(
            "--fallback", "Cannot specify more than 1 --fallback* option"
        )

    t = datetime.now().time()
    current_shader = get_screen_shader()
    shade = shader_name_or_path or schedule().find_shade(t)

    if fallback_default or (
        fallback_auto and is_same_shader(shade, schedule().find_shade(t))
    ):
        fallback = schedule().default_shade_name
    elif fallback_auto:
        fallback = schedule().find_shade(t)

    def toggle_off():
        if fallback is None:
            ctx.invoke(off)
        else:
            ctx.invoke(on, shader_name_or_path=fallback)

    if is_same_shader(shade, current_shader):
        toggle_off()
    elif shade is not None:
        ctx.invoke(on, shader_name_or_path=shade)


@cli.command()
@click.pass_context
def auto(ctx: click.Context):
    """Turn on/off screen shader based on schedule."""

    from .config import Config

    t = datetime.now().time()
    shade = Config().to_schedule().find_shade(t)

    if shade is not None:
        ctx.invoke(on, shader_name_or_path=shade)
        ctx.exit()
    ctx.invoke(off)


@cli.command()
def install():
    """Install systemd user units."""

    from .config import Config

    schedule = Config().to_schedule()

    with open(path.join(systemd_user_config_home(), "hyprshade.service"), "w") as f:
        f.write(
            """[Unit]
Description=Apply screen filter

[Service]
Type=oneshot
ExecStart="/usr/bin/hyprshade" auto"""
        )

    with open(path.join(systemd_user_config_home(), "hyprshade.timer"), "w") as f:
        on_calendar = "\n".join(
            sorted([f"OnCalendar=*-*-* {x}" for x in schedule.on_calendar_entries()])
        )
        f.write(
            f"""[Unit]
Description=Apply screen filter on schedule

[Timer]
{on_calendar}

[Install]
WantedBy=timers.target"""
        )


@cli.command()
def ls():
    """List available screen shaders."""

    current_shader = get_screen_shader()
    shader_base = path.basename(current_shader) if current_shader else None

    for shader in unique_justseen(
        sorted(
            flatten(
                map(
                    os.listdir,
                    SHADER_DIRS,
                )
            )
        )
    ):
        c = "*" if shader == shader_base else " "
        shader, _ = path.splitext(shader)
        click.echo(f"{c} {shader}")
