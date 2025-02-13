
# def except_1():
#     try:
#         1 0 *( 1 /0)
#     except Exception as e :
#     # except (RuntimeError, TypeError, NameError) as me:
#         print(e)

def except_2():
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except OSError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()
        finally:
            print("finally")

# raise 语句支持强制触发指定的异常。例如

def except_raise():
    raise NameError('HiThere')

if __name__ == '__main__':
    # except_1()
    # except_2()
    except_raise()
    pass
