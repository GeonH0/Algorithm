import Foundation

// 도화지 크기
let size = 100

// 도화지 배열 초기화
var paper = Array(repeating: Array(repeating: false, count: size), count: size)

// 색종이의 개수를 입력받음
let N = Int(readLine()!)!

// 색종이 위치 입력받아 도화지에 표시
for _ in 0..<N {
    let position = readLine()!.split(separator: " ").map { Int($0)! }
    let x = position[0]
    let y = position[1]
    
    // 색종이의 크기는 10x10
    for i in x..<x+10 {
        for j in y..<y+10 {
            paper[i][j] = true
        }
    }
}

// 도화지에서 색종이가 붙어있는 부분의 면적 계산
var area = 0
for row in paper {
    for cell in row {
        if cell {
            area += 1
        }
    }
}

// 결과 출력
print(area)




