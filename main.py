from dataclasses import dataclass


@dataclass
class TimeDelta:
    days: int = 0
    hours: int = 0
    minutes: int = 0
    seconds: int = 0

    def __str__(self):
        parts = []
        if self.days: parts.append(f"{self.days} дн")
        if self.hours: parts.append(f"{self.hours} год")
        if self.minutes: parts.append(f"{self.minutes} хв")
        if self.seconds or not parts: parts.append(f"{self.seconds} сек")
        return " ".join(parts)


def seconds_to_human(seconds: int) -> str:
    """Перетворює секунди у читабельний рядок."""
    if seconds < 0:
        return "Негативний час не підтримується"

    td = TimeDelta()
    td.days = seconds // 86400
    seconds %= 86400
    td.hours = seconds // 3600
    seconds %= 3600
    td.minutes = seconds // 60
    td.seconds = seconds % 60

    return str(td)


if __name__ == "__main__":
    print("Конвертер секунд у зрозумілий формат\n")
    try:
        secs = int(input("Кількість секунд: ").strip())
        print(f"\nЦе ≈ {seconds_to_human(secs)}")
    except ValueError:
        print("Будь ласка, введіть ціле число.")
