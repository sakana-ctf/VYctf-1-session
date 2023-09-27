source_filename = "test"
target datalayout = "e-m:e-p:64:64-i64:64-f80:128-n8:16:32:64-S128"

@global_var_4030 = global i64 0
@global_var_3fe0 = local_unnamed_addr global i64 0
@global_var_2013 = constant [3 x i8] c"%s\00"
@0 = external global i32
@1 = internal constant [15 x i8] c"\E8\AF\B7\E8\BE\93\E5\85\A5flag:\00"
@global_var_2004 = constant i8* getelementptr inbounds ([15 x i8], [15 x i8]* @1, i64 0, i64 0)
@2 = internal constant [11 x i8] c"flag\E9\94\99\E8\AF\AF\00"
@global_var_2016 = constant i8* getelementptr inbounds ([11 x i8], [11 x i8]* @2, i64 0, i64 0)
@3 = internal constant [11 x i8] c"flag\E6\AD\A3\E7\A1\AE\00"
@global_var_2021 = constant i8* getelementptr inbounds ([11 x i8], [11 x i8]* @3, i64 0, i64 0)

define i64 @_init() local_unnamed_addr {
dec_label_pc_1000:
  %rax.0.reg2mem = alloca i64, !insn.addr !0
  %0 = load i64, i64* inttoptr (i64 16336 to i64*), align 16, !insn.addr !1
  %1 = icmp eq i64 %0, 0, !insn.addr !2
  store i64 0, i64* %rax.0.reg2mem, !insn.addr !3
  br i1 %1, label %dec_label_pc_1016, label %dec_label_pc_1014, !insn.addr !3

dec_label_pc_1014:                                ; preds = %dec_label_pc_1000
  call void @__gmon_start__(), !insn.addr !4
  store i64 ptrtoint (i32* @0 to i64), i64* %rax.0.reg2mem, !insn.addr !4
  br label %dec_label_pc_1016, !insn.addr !4

dec_label_pc_1016:                                ; preds = %dec_label_pc_1014, %dec_label_pc_1000
  %rax.0.reload = load i64, i64* %rax.0.reg2mem
  ret i64 %rax.0.reload, !insn.addr !5
}

define i32 @function_1030(i8* %s) local_unnamed_addr {
dec_label_pc_1030:
  %0 = call i32 @puts(i8* %s), !insn.addr !6
  ret i32 %0, !insn.addr !6
}

define void @function_1040() local_unnamed_addr {
dec_label_pc_1040:
  call void @__stack_chk_fail(), !insn.addr !7
  ret void, !insn.addr !7
}

define i32 @function_1050(i8* %format, ...) local_unnamed_addr {
dec_label_pc_1050:
  %0 = call i32 (i8*, ...) @printf(i8* %format), !insn.addr !8
  ret i32 %0, !insn.addr !8
}

define i32 @function_1060(i8* %format, ...) local_unnamed_addr {
dec_label_pc_1060:
  %0 = call i32 (i8*, ...) @scanf(i8* %format), !insn.addr !9
  ret i32 %0, !insn.addr !9
}

define i64 @_start(i64 %arg1, i64 %arg2, i64 %arg3, i64 %arg4, i64 %arg5, i64 %arg6) local_unnamed_addr {
dec_label_pc_1070:
  %stack_var_8 = alloca i64, align 8
  %0 = trunc i64 %arg6 to i32, !insn.addr !10
  %1 = bitcast i64* %stack_var_8 to i8**, !insn.addr !10
  %2 = inttoptr i64 %arg3 to void ()*, !insn.addr !10
  %3 = call i32 @__libc_start_main(i64 4477, i32 %0, i8** nonnull %1, void ()* null, void ()* null, void ()* %2), !insn.addr !10
  %4 = call i64 @__asm_hlt(), !insn.addr !11
  unreachable, !insn.addr !11
}

define i64 @function_10a0() local_unnamed_addr {
dec_label_pc_10a0:
  ret i64 ptrtoint (i64* @global_var_4030 to i64), !insn.addr !12
}

define i64 @function_10d0() local_unnamed_addr {
dec_label_pc_10d0:
  ret i64 0, !insn.addr !13
}

define i64 @function_1110() local_unnamed_addr {
dec_label_pc_1110:
  %0 = alloca i64
  %1 = load i64, i64* %0
  %2 = load i8, i8* bitcast (i64* @global_var_4030 to i8*), align 8, !insn.addr !14
  %3 = icmp eq i8 %2, 0, !insn.addr !14
  %4 = icmp eq i1 %3, false, !insn.addr !15
  br i1 %4, label %dec_label_pc_1150, label %dec_label_pc_111d, !insn.addr !15

dec_label_pc_111d:                                ; preds = %dec_label_pc_1110
  %5 = load i64, i64* @global_var_3fe0, align 8, !insn.addr !16
  %6 = icmp eq i64 %5, 0, !insn.addr !16
  br i1 %6, label %dec_label_pc_1138, label %dec_label_pc_112b, !insn.addr !17

dec_label_pc_112b:                                ; preds = %dec_label_pc_111d
  %7 = load i64, i64* inttoptr (i64 16424 to i64*), align 8, !insn.addr !18
  %8 = inttoptr i64 %7 to i64*, !insn.addr !19
  call void @__cxa_finalize(i64* %8), !insn.addr !19
  br label %dec_label_pc_1138, !insn.addr !19

dec_label_pc_1138:                                ; preds = %dec_label_pc_112b, %dec_label_pc_111d
  %9 = call i64 @function_10a0(), !insn.addr !20
  store i8 1, i8* bitcast (i64* @global_var_4030 to i8*), align 8, !insn.addr !21
  ret i64 %9, !insn.addr !22

dec_label_pc_1150:                                ; preds = %dec_label_pc_1110
  ret i64 %1, !insn.addr !23
}

define i64 @function_1160() local_unnamed_addr {
dec_label_pc_1160:
  %0 = call i64 @function_10d0(), !insn.addr !24
  ret i64 %0, !insn.addr !24
}

define i64 @shl_flag(i64 %arg1) local_unnamed_addr {
dec_label_pc_1169:
  %0 = trunc i64 %arg1 to i32, !insn.addr !25
  %1 = ashr i32 %0, 1, !insn.addr !26
  %2 = zext i32 %1 to i64, !insn.addr !27
  ret i64 %2, !insn.addr !28
}

define i64 @main(i64 %argc, i8** %argv) local_unnamed_addr {
dec_label_pc_117d:
  %rax.0.reg2mem = alloca i64, !insn.addr !29
  %storemerge1.reg2mem = alloca i32, !insn.addr !29
  %stack_var_-88 = alloca i64, align 8
  %stack_var_-8 = alloca i64, align 8
  %0 = ptrtoint i64* %stack_var_-8 to i64, !insn.addr !30
  %1 = call i64 @__readfsqword(i64 40), !insn.addr !31
  %2 = call i32 (i8*, ...) @printf(i8* bitcast (i8** @global_var_2004 to i8*)), !insn.addr !32
  %3 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @global_var_2013, i64 0, i64 0), i64* nonnull %stack_var_-88), !insn.addr !33
  %4 = add i64 %0, -80, !insn.addr !34
  %5 = add i64 %0, -256, !insn.addr !35
  store i32 0, i32* %storemerge1.reg2mem
  br label %dec_label_pc_1352

dec_label_pc_1352:                                ; preds = %dec_label_pc_117d, %dec_label_pc_1399
  %storemerge1.reload = load i32, i32* %storemerge1.reg2mem
  %6 = sext i32 %storemerge1.reload to i64, !insn.addr !36
  %7 = add i64 %4, %6, !insn.addr !34
  %8 = inttoptr i64 %7 to i8*, !insn.addr !34
  %9 = load i8, i8* %8, align 1, !insn.addr !34
  %10 = mul i64 %6, 4, !insn.addr !35
  %11 = add i64 %5, %10, !insn.addr !35
  %12 = inttoptr i64 %11 to i32*, !insn.addr !35
  %13 = load i32, i32* %12, align 4, !insn.addr !35
  %14 = zext i32 %13 to i64, !insn.addr !37
  %15 = call i64 @shl_flag(i64 %14), !insn.addr !38
  %16 = sext i8 %9 to i32, !insn.addr !39
  %17 = trunc i64 %15 to i32, !insn.addr !39
  %18 = icmp eq i32 %16, %17, !insn.addr !39
  br i1 %18, label %dec_label_pc_1399, label %dec_label_pc_137c, !insn.addr !40

dec_label_pc_137c:                                ; preds = %dec_label_pc_1352
  %19 = call i32 @puts(i8* bitcast (i8** @global_var_2016 to i8*)), !insn.addr !41
  br label %dec_label_pc_13b6, !insn.addr !42

dec_label_pc_1399:                                ; preds = %dec_label_pc_1352
  %20 = add nuw i32 %storemerge1.reload, 1, !insn.addr !43
  %21 = icmp ult i32 %20, 41, !insn.addr !44
  store i32 %20, i32* %storemerge1.reg2mem, !insn.addr !44
  br i1 %21, label %dec_label_pc_1352, label %dec_label_pc_13a2, !insn.addr !44

dec_label_pc_13a2:                                ; preds = %dec_label_pc_1399
  %22 = call i32 @puts(i8* bitcast (i8** @global_var_2021 to i8*)), !insn.addr !45
  br label %dec_label_pc_13b6, !insn.addr !46

dec_label_pc_13b6:                                ; preds = %dec_label_pc_137c, %dec_label_pc_13a2
  %23 = call i64 @__readfsqword(i64 40), !insn.addr !47
  %24 = icmp eq i64 %1, %23, !insn.addr !47
  store i64 0, i64* %rax.0.reg2mem, !insn.addr !48
  br i1 %24, label %dec_label_pc_13ca, label %dec_label_pc_13c5, !insn.addr !48

dec_label_pc_13c5:                                ; preds = %dec_label_pc_13b6
  call void @__stack_chk_fail(), !insn.addr !49
  store i64 ptrtoint (i32* @0 to i64), i64* %rax.0.reg2mem, !insn.addr !49
  br label %dec_label_pc_13ca, !insn.addr !49

dec_label_pc_13ca:                                ; preds = %dec_label_pc_13c5, %dec_label_pc_13b6
  %rax.0.reload = load i64, i64* %rax.0.reg2mem
  ret i64 %rax.0.reload, !insn.addr !50

; uselistorder directives
  uselistorder i64 %0, { 1, 0 }
  uselistorder i32* %storemerge1.reg2mem, { 1, 0, 2 }
  uselistorder i64 0, { 0, 9, 10, 13, 2, 1, 14, 3, 4, 5, 6, 7, 8, 11, 12 }
  uselistorder label %dec_label_pc_13b6, { 1, 0 }
  uselistorder label %dec_label_pc_1352, { 1, 0 }
}

define i64 @_fini() local_unnamed_addr {
dec_label_pc_13d0:
  %0 = alloca i64
  %1 = load i64, i64* %0
  ret i64 %1, !insn.addr !51

; uselistorder directives
  uselistorder i32 1, { 1, 8, 6, 5, 3, 2, 9, 0, 7, 4 }
}

declare i32 @__libc_start_main(i64, i32, i8**, void ()*, void ()*, void ()*) local_unnamed_addr

declare void @__gmon_start__() local_unnamed_addr

declare void @__cxa_finalize(i64*) local_unnamed_addr

declare i32 @puts(i8*) local_unnamed_addr

declare void @__stack_chk_fail() local_unnamed_addr

declare i32 @printf(i8*, ...) local_unnamed_addr

declare i32 @scanf(i8*, ...) local_unnamed_addr

declare i64 @__asm_hlt() local_unnamed_addr

declare i64 @__readfsqword(i64) local_unnamed_addr

!0 = !{i64 4096}
!1 = !{i64 4104}
!2 = !{i64 4111}
!3 = !{i64 4114}
!4 = !{i64 4116}
!5 = !{i64 4122}
!6 = !{i64 4144}
!7 = !{i64 4160}
!8 = !{i64 4176}
!9 = !{i64 4192}
!10 = !{i64 4239}
!11 = !{i64 4245}
!12 = !{i64 4296}
!13 = !{i64 4360}
!14 = !{i64 4372}
!15 = !{i64 4379}
!16 = !{i64 4382}
!17 = !{i64 4393}
!18 = !{i64 4395}
!19 = !{i64 4402}
!20 = !{i64 4408}
!21 = !{i64 4413}
!22 = !{i64 4421}
!23 = !{i64 4432}
!24 = !{i64 4452}
!25 = !{i64 4461}
!26 = !{i64 4467}
!27 = !{i64 4472}
!28 = !{i64 4476}
!29 = !{i64 4477}
!30 = !{i64 4478}
!31 = !{i64 4489}
!32 = !{i64 4902}
!33 = !{i64 4929}
!34 = !{i64 4954}
!35 = !{i64 4970}
!36 = !{i64 4952}
!37 = !{i64 4977}
!38 = !{i64 4979}
!39 = !{i64 4984}
!40 = !{i64 4986}
!41 = !{i64 4998}
!42 = !{i64 5008}
!43 = !{i64 5010}
!44 = !{i64 5024}
!45 = !{i64 5036}
!46 = !{i64 5041}
!47 = !{i64 5050}
!48 = !{i64 5059}
!49 = !{i64 5061}
!50 = !{i64 5071}
!51 = !{i64 5084}
