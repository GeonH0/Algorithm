//
//  main.swift
//  Swiftalgorithm
//
//  Created by 김건호 on 8/27/24.
//

import Foundation

let nums = readLine()!.split(separator: " ").map { Int($0)! }

let N = nums[0]
let M = nums[1]

var A: [[Int]] = []
var B: [[Int]] = []

for _ in 1...N {
    let nums1 = readLine()!.split(separator: " ").map { Int($0)! }
    A.append(nums1)
}

let nums1 = readLine()!.split(separator: " ").map { Int($0)! }
let M1 = nums1[0]
let K1 = nums1[1]

for _ in 1...M1 {
    let nums1 = readLine()!.split(separator: " ").map { Int($0)! }
    B.append(nums1)
}

var C: [[Int]] = Array(repeating: Array(repeating: 0, count: K1), count: N)

// 행렬 곱셈 수행
for i in 0..<N {
    for j in 0..<K1 {
        for k in 0..<M {
            C[i][j] += A[i][k] * B[k][j]
        }
    }
}

// 결과 행렬 출력
for row in C {
    print(row.map { String($0) }.joined(separator: " "))
}
