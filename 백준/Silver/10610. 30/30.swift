//
//  main.swift
//  Swiftalgorithm
//
//  Created by 김건호 on 9/10/24.
//

import Foundation

let N = readLine()!

var digits = N.compactMap { Int(String($0))}

if digits.contains(0) {
    let sum = digits.reduce(0, +)
    if sum % 3 == 0 {
        digits.sort(by: >)
        print(digits.map {String($0)}.joined())
    } else {
        print(-1)
    }
} else {
    print(-1)
}
