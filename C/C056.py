def main():
    m, n = map(int, input().split())
    
    for i in range(1, m+1):
        a, b = map(int, input().split())
        
        grade = a - (5 * b)
        
        if grade < 0:
            grade = 0
        
        if n <= grade:
            print(i)
    
if __name__ == '__main__':
    main()