def _if(bool, truthy, falsey):
    if bool:
        return truthy()
    else:
        return falsey()


def truthy():
    print("True")


def falsey():
    print("False")


_if(True, truthy, falsey)
