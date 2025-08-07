import os

try:
    # python-dotenv is an optional dependency; provide a graceful fallback when
    # it is not available so importing this module does not raise an error.
    from dotenv import load_dotenv  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - simple fallback
    def load_dotenv(*_args, **_kwargs):  # type: ignore
        return None


# Load environment variables from a .env file if present.  This is executed
# unconditionally, but when ``load_dotenv`` is the no-op fallback above, it has
# no effect.
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

def get_env(key: str, default=None):
    return os.getenv(key, default)
