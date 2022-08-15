n, s = map(int, input().split())
arr = list(int(input()) for _ in range(n))
arr.sort(reverse=True) #내림차순 정렬 => C언어는 qsort(arr, n, sizeof(int), compare), compare함수 새로 만들어야 함
cnt, start = 0, 0
while start < n:
    for i in range(start, n-1):
        if arr[start] + arr[i+1] <= s:
            cnt += n - (i+1) #start인덱스에서의 소의 다음 소부터 더한 값이 s보다 같거나 작으면 이후 소들과 사이즈를 더한 값은 무조건 작음. 따라서 n에서 (i+1)만큼 빼 준 값을 더하고 break
            break
    start += 1
print(cnt)
'''int compare(const void *p,const void *q){
        if(*(int *)p>*(int *)q)
                return 1;
        else if(*(int *)p<*(int *)q)
                return -1;
        return 0;
}'''