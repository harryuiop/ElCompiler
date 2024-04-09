.class public Program
.super java/lang/Object
.method public <init>()V
aload_0
invokenonvirtual java/lang/Object/<init>()V
return
.end method
.method public static main([Ljava/lang/String;)V
.limit locals 4
.limit stack 1024
new java/util/Scanner
dup
getstatic java/lang/System.in Ljava/io/InputStream;
invokespecial java/util/Scanner.<init>(Ljava/io/InputStream;)V
astore 0
aload 0
invokevirtual java/util/Scanner.nextInt()I
istore 1
aload 0
invokevirtual java/util/Scanner.nextInt()I
istore 2
sipush 0
istore 3
iload 1
iload 2
if_icmpge l1
iload 1
istore 3
l1:
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 3
invokestatic java/lang/String/valueOf(I)Ljava/lang/String;
invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
return
.end method
