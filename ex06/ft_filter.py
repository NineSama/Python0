def ft_filter(function, iterable):
    """
    Objective:
        Custom function ft_filter that behaves like
        the original built-in filter() function
    Return:
        iter(): returns an iterator with iter()
    """
    if function is None:
        return iter([item for item in iterable if item])
    return iter([item for item in iterable if function(item)])
