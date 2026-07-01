import  sys

def ft_kaboom_1() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_book

        dark_spell_record("Void", "bats")
    except ImportError as e:
        import traceback

        tb = e.__traceback__
        extracted_entries = traceback.extract_tb(tb)

        print("Traceback (most recent call): ")
        for entry in extracted_entries:
            print(
                f'  File "{entry.filename}", line {entry.lineno}, '
                f"in {entry.name}"
            )
            if entry.line:
                print(f"    {entry.line}")

        print(f"{type(e).__name__}: {e}")
        sys.exit(0)

if  __name__=="__main__":
    ft_kaboom_1()