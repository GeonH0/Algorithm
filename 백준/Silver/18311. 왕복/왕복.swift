import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0]
var K = input[1]

let value = readLine()!.split(separator: " ").map { Int($0)! }
let sum = value.reduce(0, +)

// K를 전체 코스 왕복 거리보다 작은 값으로 처리 (왕복 고려)
K = K % (sum * 2)

var currentSum = 0
var direction = 1 // 1: 순방향, -1: 역방향

if K > sum {
    K = K - sum // 역방향으로 K 값을 재설정
    direction = -1
}

// 코스 찾기
if direction == 1 {
    // 순방향
    for i in 0..<N {
        currentSum += value[i]
        if K < currentSum {
            print(i + 1)
            break
        }
    }
} else {
    // 역방향
    for i in stride(from: N - 1, through: 0, by: -1) {
        currentSum += value[i]
        if K < currentSum {
            print(i + 1)
            break
        }
    }
}