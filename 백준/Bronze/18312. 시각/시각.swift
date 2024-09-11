//
//  main.swift
//  Swiftalgorithm
//
//  Created by 김건호 on 9/11/24.
//

import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let maxHour = input[0]  // N
let target = String(input[1])  // K를 문자열로 변환

var count = 0

// 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중 K가 포함된 경우 세기
for i in 0...maxHour {
    for j in 0..<60 {
        for k in 0..<60 {
            // 시, 분, 초를 두 자리 문자열로 변환하여 확인
            let timeString = String(format: "%02d%02d%02d", i, j, k)
            if timeString.contains(target) {
                count += 1
            }
        }
    }
}

print(count)
