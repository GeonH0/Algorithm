//
//  main.swift
//  Swiftalgorithm
//
//  Created by 김건호 on 9/10/24.
//

import Foundation

let n = Int(readLine()!)!

if n == 1 {
    print(0)
} else {
    var dp = Array(repeating: 0, count: n+1)

    for i in 2...n {
        dp[i] = dp[i-1] + 1
        
        if i % 2 == 0 {
            dp[i] = min(dp[i], dp[i/2] + 1)
        }
        if i % 3 == 0 {
            dp[i] = min(dp[i], dp[i/3] + 1)
        }
    }

    print(dp[n])
}
