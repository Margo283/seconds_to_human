def seconds_to_readable(total_seconds):
    if total_seconds < 0:
        return "Негативний час?"
    
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    parts = []
    if days:    parts.append(f"{days} дн")
    if hours:   parts.append(f"{hours} год")
    if minutes: parts.append(f"{minutes} хв")
    if seconds or not parts: parts.append(f"{seconds} сек")
    
    return " ".join(parts)


if __name__ == "__main__":
    print("Перетворювач секунд у зрозумілий вигляд\n")
    try:
        secs = int(input("Введи кількість секунд: "))
        print(f"\nЦе ≈ {seconds_to_readable(secs)}")
    except ValueError:
        print("Потрібно число")
