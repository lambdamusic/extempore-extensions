

def gen_names(prefix, start, end):
    """Generates output like this

    ;; bd samples 20-29
    (define bd0 20)
    (define bd1 21)
    (define bd2 22)
    (define bd3 23)
    (define bd4 24)
    (define bd5 25)
    (define bd6 26)
    (define bd7 27)
    (define bd8 28)
    (define bd9 29)
    """
    print(f";;\n;; {prefix} samples {start}-{end}")
    counter = 0
    for x in range(start, end+1):
        name = f"{prefix}{counter}"
        line = f"(define {name} {x})"
        counter += 1
        print(line)


# ;; dystopia
gen_names("bd", 1, 24)
gen_names("sn", 25, 58)
gen_names("hh", 59, 101)
gen_names("cy", 102, 108)
gen_names("cr", 109, 118)
gen_names("cl", 119, 123)
gen_names("co", 124, 125)
gen_names("tr", 126, 126)