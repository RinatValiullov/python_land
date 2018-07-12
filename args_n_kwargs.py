def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# first with *args
args = ("two", 4, 5)
test_args_kwargs(*args)

print("***************")

# now with **kwargs
kwargs = {"arg3": 3, "arg2": "two", "arg1": 1}
test_args_kwargs(**kwargs)

print("***************")


def test_args_kwargs1(args):
    for key, value in args.items():
        print("{0} = {1}".format(key, value))


an_kwargs = {'a': 1, 'b': 2, 'c': 3}
test_args_kwargs1(an_kwargs)
