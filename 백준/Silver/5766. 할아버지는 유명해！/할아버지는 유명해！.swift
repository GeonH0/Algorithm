//
//  main.swift
//  Swiftalgorithm
//
//  Created by 김건호 on 9/20/24.
//

import Foundation

while true {
    let value = readLine()!.split(separator: " ").map { Int($0)! }
    let N = value[0]
    let M = value[1]
    var rank : [Int:Int] = [:]
    
    if N == 0 && M == 0 {
        break
    } else {
        for _ in 0..<N {
            let weekrank = readLine()!.split(separator: " ").map { Int($0)! }
            for i in 0..<M {
                if rank.keys.contains(weekrank[i]) {
                    rank[weekrank[i]]! += 1
                } else {
                    rank[weekrank[i]] = 1
                }
            }
        }
        
        let sortedRanks = rank.values.sorted(by: >)
        
        var result : [Int] = []
        for (key,value) in rank {
            if value == sortedRanks[1] {
                result.append(key)
            }
        }
        result.sort()
        print(result.map { String($0) }.joined(separator: " "))
    }
}

