# Your PC ran into a problem and needs to restart

Before you start, you might want to download the symbols by adding "srv*https://msdl.microsoft.com/download/symbols" to symbol path

1. When was the dump captured? [mm/dd/yyyy]
    -  ans: **10/18/2009**

    open the dump file in Windbg and you will find
    ```
    Debug session time: Sun Oct 18 05:46:51.399 2009 (UTC + 7:00)
    ```

2. What is the bug check code and its name? [0xcode:name]
    - ans: **0xF4:CRITICAL_OBJECT_TERMINATION**

    run `!analyze -v` and you will find `CRITICAL_OBJECT_TERMINATION (f4)`

3. What is the name of the terminated process?
    - ans: **csrss.exe**
    
    run `!analyze -v` and you will find
    ```
    Key  : CriticalProcessDied.Process
    Value: csrss.exe
    ```
    or if you check the Arg3 stores "Process image file name", then you can run `db fffffa800aebbb28`

4. What is the kernel version?
    - ans: **6.0.6002.18005**

    run `lmdv` to display information about loaded modules in the target process. The first one come up is module "nt", and you will find its version right under image size.
    ```
    ImageSize:        00518000
    File version:     6.0.6002.18005
    Product version:  6.0.6002.18005
    ```

5. What is the address of the exceptions handler function? [0xaddress]
    - ans: **0xfffff80001e71ffc**
    
    run `kb`, you will get `fffff80001e720a5` as `nt!KiExceptionDispatch+0xa9`.
    ```
    #  RetAddr               : Args to Child                                                           : Call Site
    00 fffff800`02172353     : 00000000`000000f4 00000000`00000003 fffffa80`0aebb8f0 fffffa80`0aebbb28 : nt!KeBugCheckEx
    01 fffff800`0208b358     : fffffa80`0aeafbb0 fffffa80`0aeafbb0 fffffa60`05423c20 fffffa60`05423a40 : nt!PspCatchCriticalBreak+0x93
    02 fffff800`020bef50     : fffffa80`0aeafbb0 00000000`00000008 fffffa60`05423c20 00000000`00000008 : nt! ?? ::NNGAKEGL::`string'+0x110f6
    03 fffff800`01e72ef3     : fffffa80`0aebb8f0 fffffa80`0aeafbb0 fffffa60`05423320 fffffa60`05423c20 : nt!NtTerminateProcess+0xd8
    04 fffff800`01e73400     : fffff800`01ed32cd fffffa60`05423b78 fffffa60`05423ca0 fffffa60`05423c20 : nt!KiSystemServiceCopyEnd+0x13
    05 fffff800`01ed32cd     : fffffa60`05423b78 fffffa60`05423ca0 fffffa60`05423c20 00000000`00af1990 : nt!KiServiceLinkage
    06 fffff800`01e732a9     : fffffa60`05423b78 00000000`0001a500 fffffa60`05423c20 00000000`00af2148 : nt! ?? ::FNODOBFM::`string'+0x2935c
    07 fffff800`01e720a5     : 00000000`00000001 00000000`00000000 00000000`00000001 00000000`0001a500 : nt!KiExceptionDispatch+0xa9
    08 00000000`76e49790     : 00000000`00000000 00000000`00000000 00000000`00000000 00000000`00000000 : nt!KiPageFault+0x1e5
    09 00000000`00000000     : 00000000`00000000 00000000`00000000 00000000`00000000 00000000`00000000 : 0x76e49790
    ```
    Substract 0xfffff80001e720a5 with 0xa9 and you will get the actual address of KiExceptionDispatch.
