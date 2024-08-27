//
//  main.swift
//  Swiftalgorithm
//
//  Created by 김건호 on 8/27/24.
//

import Foundation

let input = readLine()!
let K = Int(input)!

var dung: [[Int]] = []

for _ in 1...K {
    let nums = readLine()!.split(separator: " ").map { Int($0)! }
    let x = nums[0]
    let y = nums[1]
    dung.append([x,y])
}

var ans: [Int] = Array(repeating: 1, count: K)

// 모든 사람을 비교하여 등수 계산
for i in 0..<K {
    for j in 0..<K {
        if i != j {
            if dung[i][0] < dung[j][0] && dung[i][1] < dung[j][1] {
                ans[i] += 1
            }
        }
    }
}

print(ans.map { String($0) }.joined(separator: " "))
