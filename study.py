import tkinter as tk
# memo = [0 if i == 0 else 1 if i == 1 else None for _ in range(100)]
memo = [0, 1] + [None] * (100 - 1)


def fibo_memoization(
    number: int,
) -> int:  # 동적프로그래밍: 공간이 소모되더라도 프로그램의 속도를 높이기 위해 사용
    """
    fibonacci function by recursion with memoization.
    :param number: integer number
    :return: integer number
    """
    global memo
    if memo[number] is not None:
        return memo[number]
    result = fibo_memoization(number - 1) + fibo_memoization(number - 2)
    memo[number] = result
    return result

def process_fibonacci():
    number = int(en_input_numver.get())
    lbl_display_fibonacci_result.config(text=f"fibo({number}) = {fibo_memoization(number)}")


if __name__ == '__main__':
    w = tk.Tk() # create window object
    w.title('Fibonacci by memoization') # set title
    w.geometry('400x200') # set size

    #create widgets
    lbl_display_fibonacci_result = tk.Label(w, text='Fibonacci by memorizaiton')
    en_input_numver = tk.Entry(w)
    btn_click = tk.Button(w, text='Click', command=process_fibonacci)
    
    #layout
    lbl_display_fibonacci_result.pack()
    en_input_numver.pack(fill='x')
    btn_click.pack(fill='x')

    en_input_numver.focus_set()
    w.mainloop()

# n = int(input("Input number : "))
# print(f'f({n}) = {fibo_memoization(n)}')
