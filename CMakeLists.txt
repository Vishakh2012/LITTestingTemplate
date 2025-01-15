#cmake list linking against mlir , llvm and other dependencies for creating a dialect

cmake_minimum_required(VERSION 3.13)
project(MLIRHelloWorld)

set(CMAKE_CXX_STANDARD 17)

# Find MLIR
# This can be removed once MLIR is properly installed on your system
#list(APPEND CMAKE_MODULE_PATH "${MLIR_DIR}")
#find_package(MLIR REQUIRED CONFIG)

# LLVM is a transitive dependency of MLIR
find_package(LLVM REQUIRED CONFIG)

# Add the MLIR and LLVM include directories
#include_directories(${MLIR_INCLUDE_DIRS})
include_directories(${LLVM_INCLUDE_DIRS})

add_subdirectory(test)
