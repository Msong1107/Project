window.dd = console.log.bind(console);

window.onload = () => {

    let user = 1;
    let cnt = 0;
    let data = [[null, null, null], [null, null, null], [null, null, null]]

    let square = document.querySelectorAll('.box');
    let result = document.querySelector('#result > span');

    (function check() {

        square.forEach((el, ix) => {

            el.addEventListener('click', function (e) {
                if (e.target.innerHTML === '') {
                    cnt += 1;
                    if (user) {
                        this.innerHTML = "O";
                        user = 0;
                    } else {
                        this.innerHTML = "X";
                        user = 1;
                    }

                    data[+this.parentNode.dataset.name].splice(this.dataset.location, 1, this.innerHTML);
                }

                clear();
            });
        });
    })();

    function clear() {

        // 대각선
        if ((data[0][0] === "O" && data[1][1] === "O" && data[2][2] === "O") || (data[0][2] === "O" && data[1][1] === "O" && data[2][0] === "O"))
            result.innerHTML = 'player O 님이 이기셨습니다.';

        if ((data[0][0] === "X" && data[1][1] === "X" && data[2][2] === "X") || (data[0][2] === "X" && data[1][1] === "X" && data[2][0] === "X"))
            result.innerHTML = 'player X 님이 이기셨습니다.';

        // 가로세로
        for (var i = 0; i <= 2; i++) {
            if (data[0][i] === "O" && data[1][i] === "O" && data[2][i] === "O" || data[i][0] == "O" && data[i][1] === "O" && data[i][2] === "O")
                result.innerHTML = 'player O 님이 이기셨습니다.';

            if (data[0][i] === "X" && data[1][i] === "X" && data[2][i] === "X" || data[i][0] == "X" && data[i][1] === "X" && data[i][2] === "X")
                result.innerHTML = 'player X 님이 이기셨습니다.';
        }
    }
}