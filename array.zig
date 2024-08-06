const std = @import("std");
const print = std.debug.print;

export fn test_arr_func(arr: [*c]f64, n_rows: usize, n_cols: usize) void {
    print("test: {d}\n", .{arr[1]});
    for (0..n_rows) |i| {
        for (0..n_cols) |j| {
            print("arr[{d}], [{d}] -> ", .{ i, j });
            print("cell value: {d}\n", .{arr[i * n_rows + j]});
        }
    }
    print("hello crazy people!\n", .{});
}

export fn test_2darr_func(arr1: [*c][*c]f64, arr2: [*c][*c]f64, n_rows: usize, n_cols: usize) void {
    for (0..n_rows) |i| {
        for (0..n_cols) |j| {
            arr2[i][j] = arr1[i][j] - 1;
        }
    }
    print("hello crazy people!\n", .{});
}

export fn test_3darr_func(arr1: [*c][*c][*c]f64, arr2: [*c][*c][*c]f64, n_rows: usize, n_cols: usize, n_levels: usize) void {
    for (0..n_rows) |i| {
        for (0..n_cols) |j| {
            for (0..n_levels) |k| {
                arr2[i][j][k] = arr1[i][j][k] - 1;
            }
        }
    }
    print("hello crazy people!\n", .{});
}
