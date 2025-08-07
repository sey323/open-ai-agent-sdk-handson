"""Entry point for running the sample OpenAI agent.

This module exposes a synchronous ``main`` function that launches the
asynchronous quick start triage agent.  Tests rely on the presence of this
module and its ``main`` function so that ``open_ai_agent_sample.main`` can be
imported without error.
"""

import asyncio


def main() -> None:
    """Run the quick start triage agent using ``asyncio``.

    Importing the heavy ``quick_start`` module is deferred until runtime so
    that simply importing ``open_ai_agent_sample.main`` does not require the
    optional ``agents`` package.  This mirrors typical CLI entry points where
    the bulk of the work happens only when ``main`` is executed.
    """
    from open_ai_agent_sample.agents.quick_start.main import main as _quick_start_main

    asyncio.run(_quick_start_main())


if __name__ == "__main__":
    main()
