# Elementals

  <p align="justify">Forces of Nature</p>
  
## Step 2 Solve
1. This challenge is a standard heap-note, with heap-overflow bug
2. With the heap-overflow, you can overwrite anychunk metadata.
3. In here, you can only allocate up to 7 bytes, so you can't get out of t-cache.
4. Even if you somehow manage to get an allocation outside of t-cache's and fastbin's size, you can't free it because of the size "protection".
5. So, the only way (afaik) to get a leak is by abusing the top chunk.
6. We can use a technique called [sysmalloc_int_free](https://github.com/shellphish/how2heap/blob/master/glibc_2.39/sysmalloc_int_free.c)
7. Using that technique, you can shrink the top chunk, and get a chunk in the unsorted bin (some heap grooming and calculation needed).
8. After that, you can get a libcleak using the overflow.
9. After that, just t-cache poisoning to `libc.environ` (don't forget to bypass safe-linking)
10. Then leak the stack address in libc.environ
11. Then just t-cache poison to RIP of main, edit the data and send your ROP chain.
