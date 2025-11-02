"""Command-line interface for blockbt."""
import click
import sys


@click.group()
@click.version_option(version="0.1.0-mvp", prog_name="bbt")
def cli():
    """BlockBT - Blockchain data transformation tool."""
    pass


@cli.command()
@click.argument("targets", nargs=-1)
@click.option("--select", "-s", multiple=True, help="Select models to run")
@click.option("--full-refresh", is_flag=True, help="Full refresh mode")
def run(targets, select, full_refresh):
    """Run models."""
    click.echo("Running models...")
    if targets:
        click.echo(f"Targets: {targets}")
    if select:
        click.echo(f"Selected models: {select}")
    if full_refresh:
        click.echo("Full refresh mode enabled")
    # TODO: Implement actual run logic
    click.echo("✓ Run completed!")


@cli.command()
@click.argument("targets", nargs=-1)
@click.option("--select", "-s", multiple=True, help="Select models to compile")
def compile(targets, select):
    """Compile SQL models."""
    click.echo("Compiling models...")
    if targets:
        click.echo(f"Targets: {targets}")
    if select:
        click.echo(f"Selected models: {select}")
    # TODO: Implement actual compile logic
    click.echo("✓ Compilation completed!")


@cli.command()
@click.argument("targets", nargs=-1)
@click.option("--select", "-s", multiple=True, help="Select models to test")
def test(targets, select):
    """Run tests on models."""
    click.echo("Running tests...")
    if targets:
        click.echo(f"Targets: {targets}")
    if select:
        click.echo(f"Selected models: {select}")
    # TODO: Implement actual test logic
    click.echo("✓ Tests completed!")


@cli.command()
@click.option("--adapter", default="ethereum", help="Adapter to initialize")
def init(adapter):
    """Initialize a new BlockBT project."""
    click.echo(f"Initializing BlockBT project with {adapter} adapter...")
    # TODO: Implement actual init logic
    click.echo("✓ Project initialized!")


def run():
    """Entry point for the bbt command."""
    cli()


if __name__ == "__main__":
    run()

