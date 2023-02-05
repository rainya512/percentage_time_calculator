import datetime
import time
import os


# 계산기의 모드 설정
def select_mode():
    while True:
        # 모드 설정을 위해 숫자 입력
        mode = int(input("모드를 설정하세요 (1:자동모드 2:수동모드) >> "))

        if 0 < mode < 3:
            return mode
        else:
            print("잘못 입력했습니다. 다시 입력하세요.")


# 날짜를 입력받는다.
def input_day(case):
    while True:
        # 입력부
        year, month, day = input("날짜를 입력하세요 >> ").split()
        year = int(year)
        month = int(month)
        day = int(day)

        # 입력한 날짜가 가능한 경우인지 판별
        if correct_day(year, month, day):
            # 가능한 경우 입력받은 날짜를 유닉스 타임으로 변환(불가능하면 에러 발생함)
            day_time = datetime.datetime(year, month, day).timestamp()

            # case 0:시작 지점
            if case == 0:
                # 시작 시점이 현재보다 미래라면 오류 메시지 출력
                if day_time > datetime.datetime.today().timestamp():
                    print("%s 혹은 보다 이전의 날짜를 입력하세요." % time.strftime("%Y/%m/%d", time.localtime(
                        datetime.datetime.today().timestamp())))
                else:
                    return day_time

            # case 1:끝 지점
            if case == 1:
                # 끝 지점이 현재보다 과거라면 오류 메시지 출력
                if day_time < datetime.datetime.today().timestamp():
                    print("%s 이후의 날짜를 입력하세요." % time.strftime("%Y/%m/%d",
                                                              time.localtime(datetime.datetime.today().timestamp())))
                else:
                    return day_time
        # 불가능한 경우 오류 메시지 출력
        else:
            print("잘못 입력했습니다. 다시 입력하세요.")


# 날짜를 올바르게 입력했는지 판별하는 함수
def correct_day(y, m, d):
    # 월을 잘못 입력했을 경우
    if m <= 0 or m > 12:
        return False
    # 일을 잘못 입력했을 경우
    elif m in [1, 3, 5, 7, 8, 10, 12] and d > 31 or m in [4, 6, 9, 11] and d > 30 or m == 2 and (
            y % 4 == 0 or y % 400 == 0) and d > 29 or m == 2 and (
            y % 4 != 0 or y % 100 == 0) and d > 28:
        return False
    else:
        return True


# 날짜 변환 함수
def next_day(y, m, d):
    # 다음날로 변환
    d += 1
    # 불가능한 날짜일 경우
    if not correct_day(y, m, d):
        d = 1
        m += 1
        # 월에 대해 재검사
        if not correct_day(y, m, d):
            y += 1
            m = 1

    # 튜플 형태로 return (더 나은 형태를 찾지 못함)
    return y, m, d


# 로직 작동부
def select_type(is_auto, type):
    # 시작 지점과 끝 지점 변수 할당(IDE에서 경고가 떴음...)
    start = 0.0
    end = 0.0

    # 연도를 받아온다.
    current_year = datetime.datetime.today().year

    # 자동 모드:시작 지점과 끝 지점을 미리 정해둔 모드
    if is_auto:
        # "올해 몇% 지났지?" 모드(auto - 1)
        if type == 1:
            print("시작일을 올해 1월 1일로 합니다.")
            print("D - day를 내년 1월 1일로 합니다.")

            # 현재 연도를 받아오고 시작/끝 지점에 적용
            start = datetime.datetime(current_year, 1, 1).timestamp()
            end = datetime.datetime(current_year+1, 1, 1).timestamp()
        # "오늘 몇% 지났지?" 모드(auto - 3)
        elif type == 2:
            print("시작일을 오늘로 합니다.")
            print("D - DAY를 내일로 합니다.")

            # 현재 시각을 받아와 연/월/일 형태로 변환해 시작 지점에 적용
            date = datetime.datetime.today()
            start = datetime.datetime(date.year, date.month, date.day).timestamp()
            # 날짜 변환 함수를 이용해 다음날을 구하고 끝 지점에 적용
            date = next_day(date.year, date.month, date.day)
            end = datetime.datetime(date[0], date[1], date[2]).timestamp()

    # 수동 모드: 시작 지점 또는 끝 지점을 직접 입력할 수 있는 모드
    else:
        # 시작 지점을 1월 1일로 설정(manual - 1)
        if type == 1:
            print("시작일을 올해 1월 1일로 합니다.")
            start = datetime.datetime(current_year, 1, 1).timestamp()
            print("D - day를 입력합니다.")
            end = input_day(1)
        # 시작 지점을 현재 시각으로 설정(manual - 2)
        elif type == 2:
            print("시작일을 현재 시각으로 합니다.")
            start = datetime.datetime.today().timestamp()
            print("D - day를 입력합니다.")
            end = input_day(1)
        # 시작 지점을 직접 입력(manual - 3)
        elif type == 3:
            print("시작일을 입력합니다.")
            start = input_day(0)
            print("D - day를 입력합니다.")
            end = input_day(1)

    # 출력부 함수 실행
    time.sleep(1.5)
    timer(start, end)


# 출력부 함수
def timer(day1, day2):
    # 변수 선언
    per_time = 0

    while per_time < 100:
        # 현재 시간을 받아온다.
        current_time = datetime.datetime.today().timestamp()
        # 실제 계산 연산 진행
        per_time = ((current_time - day1) / (day2 - day1)) * 100

        # 출력부
        print("현재 시각")
        print(time.strftime("%Y/%m/%d %a  %I:%M:%S %p", time.localtime(current_time)))
        print("\t")
        print("D - DAY")
        print(time.strftime("%Y/%m/%d %a", time.localtime(day2)))
        print("\t")
        print("%s부터 %s까지 %.6f%% 지났습니다." % (
            time.strftime("%Y/%m/%d", time.localtime(day1)), time.strftime("%Y/%m/%d", time.localtime(day2)), per_time))
        # 1초 주기로 실행
        time.sleep(1)
        os.system('cls')

    # 100%에 도달했을 때 프로그램을 다시 시작할지 묻기
    while True:
        con = input("100%에 도달했습니다. 프로그램을 다시 시작할까요? (y/n) >> ")

        if con == 'y':
            os.system('cls')
            main()
        elif con == 'n':
            os.system('exit')
        else:
            print("잘못 입력했습니다. 다시 입력하세요.")


def main():
    # 모드 선택부에서 넘겨받기
    num = select_mode()

    while True:
        # 상세 모드 설정
        # 자동 모드 옵션 선택(숫자 입력)
        if num == 1:
            type = int(input("원하는 계산기를 선택하세요 (1:1년 2:하루) >> "))

            if 0 < type < 3:
                select_type(True, type)
            else:
                print("잘못 입력했습니다. 다시 입력하세요.")
        # 수동 모드 옵션 선택(숫자 입력)
        elif num == 2:
            type = int(input("원하는 시작일을 선택하세요 (1:2022년 1월 1일 2:현재 시각 3:직접 입력) >> "))

            if 0 < type < 4:
                select_type(False, type)
            else:
                print("잘못 입력했습니다. 다시 입력하세요.")


if __name__ == "__main__":
    main()
