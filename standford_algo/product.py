def karatsuba(n1, n2):

    n1_str = str(n1)
    n2_str = str(n2)
    n1_len = len(n2_str)
    n2_len = len(n1_str)
    max_len = max(n1_len, n2_len)

    if n1 < 10 or n2 < 10:
        return n1 * n2
    else:
        half = max_len // 2
        n1_str = ''.join(list('0' * max_len)
                         [0: -n1_len] + list(n1_str))
        n2_str = ''.join(list('0' * max_len)
                         [0: -n2_len] + list(n2_str))

        print(n1_str, n2_str)

        a = int(n1_str[0: -half])
        b = int(n1_str[-half:])
        c = int(n2_str[0: -half])
        d = int(n2_str[-half:])

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        a_plus_b_times_c_plus_d = karatsuba(a + b, c + d)
        ad_plus_bc = a_plus_b_times_c_plus_d - ac - bd

        res = ac * 10 ** (half*2) + \
            bd + \
            ad_plus_bc * 10 ** half

        return res


if __name__ == "__main__":
    res = karatsuba(5678, 1234)
    assert res == 5678 * 1234
    # print(res)
    res = karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                    2718281828459045235360287471352662497757247093699959574966967627)
    assert res == 3141592653589793238462643383279502884197169399375105820974944592 * \
        2718281828459045235360287471352662497757247093699959574966967627
    print(res)