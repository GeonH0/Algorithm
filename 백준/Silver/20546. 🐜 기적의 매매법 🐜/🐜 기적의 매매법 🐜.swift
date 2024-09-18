//
//  main.swift
//  Swiftalgorithm
//
//  Created by 김건호 on 9/18/24.
//

import Foundation

let money = Int(readLine()!)!

var value = readLine()!.split(separator: " ").map { Int($0)! }

var Jm = money
var Sm = money
var Jv = 0
var Sv = 0
var cnt : [Int] = []

for i in value {
    
    cnt.append(i)
    
    if Jm >= i {
        while Jm >= i {
            Jv += 1
            Jm -= i
        }
    }
    
    if cnt.count >= 4 {
        for j in 3..<cnt.count {
            if cnt[j-3] > cnt[j-2] && cnt[j-2] > cnt [j-1] && cnt[j-1] > cnt[j] {
                while Sm >= i {
                    Sv += 1
                    Sm -= i
                }
            }
            else if cnt[j-3] < cnt[j-2] && cnt[j-2] < cnt [j-1] && cnt[j-1] < cnt[j] {
                if Sv > 0 {
                    Sm += i * Sv
                    Sv = 0
                }
            }
        }
    }
}

if Sm + Sv*cnt[cnt.count-1] > Jm + Jv*cnt[cnt.count-1] {
    print("TIMING")
} else if Sm + Sv*cnt[cnt.count-1] < Jm + Jv*cnt[cnt.count-1] {
    print("BNP")
} else if Sm + Sv*cnt[cnt.count-1] == Jm + Jv*cnt[cnt.count-1] {
    print("SAMESAME")
}


