set(LIT_TEST_DIR ${CMAKE_CURRENT_SOURCE_DIR})

message(MLIR_INCLUDE_DIR: ${MLIR_INCLUDE_DIR})
message(ENABLE_PYTHON_BINDINGS: ${ENABLE_PYTHON_BINDINGS})
configure_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/lit.site.cfg.py.in
    ${CMAKE_CURRENT_SOURCE_DIR}/lit.site.cfg.py
    @ONLY
)

add_custom_command(
    OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/test/test.log
    COMMAND lit -v ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "running test files"
)

add_custom_target(lit-test
    DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/test/test.log
)

