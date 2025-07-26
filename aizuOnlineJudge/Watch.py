def main():
    S = int(input())
    hour = S // 3600
    S -= 3600 * hour
    minute = S // 60
    S -= 60 * minute
    second = S

    print(hour, ":", minute, ":", second, sep="")


if __name__ == "__main__":
    main()

    """
    h = s // 3600
    m = s % 3600 // 60
    s = s % 60
    でよかった
    """
