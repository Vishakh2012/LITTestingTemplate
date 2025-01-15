// RUN: mlir-opt %s --convert-math-to-funcs=convert-ctlz | /home/vishforit/llvm-project/build/bin/FileCheck %s 
func.func @main(%arg0: i32) -> i32 {
    // CHECK: call
    // CHECK: return
    //CHECK:holo
    %0 = math.ctlz %arg0 : i32
    func.return %0 : i32
}
