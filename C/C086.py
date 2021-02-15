def main():
    s = input()
    
    boin = ('a', 'i', 'u', 'e', 'o')
    ans = ''
    
    for c in s:
        if not c.lower() in boin:
            ans += c
            
    print(ans)

    
if __name__ == '__main__':
    main()