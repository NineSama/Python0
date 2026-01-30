import os


def ft_tqdm(lst: range) -> None:
    """
    Objective:
        Custom function ft_tqdm that behaves like
        the original tqdm progress bar
    """
    total = len(lst)
    term_width = os.get_terminal_size().columns
    bar_width = min(50, term_width - 20)

    for i, item in enumerate(lst):
        percent = (i + 1) / total
        filled = int(bar_width * percent)
        bar = '█' * filled + ' ' * (bar_width - filled)
        print(
            f'\r{int(percent*100):3}%|[{bar}]| {i}/{total}', end='', flush=True
            )
        yield item

    print()
