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


if __name__ == "__main__":
    print(main(b"OK"))
