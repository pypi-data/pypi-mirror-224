cmake_minimum_required(VERSION 3.26)
project(pytun C)

set(CMAKE_C_STANDARD 11)

include_directories(.
        /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Headers/)

add_executable(pytun
        darwin_pytun.c
        common.h
        linux_pytun.c)
