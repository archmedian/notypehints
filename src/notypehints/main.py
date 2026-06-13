def main(data: bytes) -> str:
    try:
        if len(data) > 1000:
            raise ValueError("Input too large")

        text = data.decode("utf-8")
        if text == "OK":
            return "OK"
        elif "bad" in text:
            raise RuntimeError("Found forbidden word")
        else:
            return "NOT OK"
    except UnicodeDecodeError:
        return "NOT OK"
    except Exception as e:
        return f"Error: {str(e)}"


def dummy_age_valid(age):
    if age < 18:
        raise ValueError("Age must be 18 or more")
    return True


if __name__ == "__main__":
    print(main(b"OK"))
