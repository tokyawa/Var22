/*переменная подсчета кликов по кнопке*/
let clicks = 0;
/*константа, устанавливающая время игры (в нашем случае 6000 мс = 6 секундам)*/
const TIMEOUT = 6000;
/*константы хранящие ссылки на элементы отображения времени, кнопки, счетчика кликов*/
const display = document.querySelector('#display');
const button = document.querySelector('#button');
const counter = document.querySelector('#counter');

button.onclick = start;
/*начало*/
function start() {
    /*фиксируется время начала*/
    const startTime = Date.now();
    /*время игры (в нашем случае 6 сек) отображается на экране*/
    display.textContent = formatTime(TIMEOUT);
    /*так называемый счетчик (как работает? при каждом клике на кнопку
    переменная увеличивается и кол-во кликов выводится на экран*/
    button.onclick = () => counter.textContent = clicks++;
    /*обновление таймера! каждые 100 мс обновляется отображение оставшегося времени на экране*/
    const interval = setInterval (() => {
        const delta = Date.now() - startTime;
        display.textContent = formatTime(TIMEOUT - delta);
    }, 100);
    /*по истечении 6 секунд (6000 мс) игра останавливается;
    вывод сообщения "Игра Завершена"; счетчик времени обнуляется (удаляется)*/
    const timeout = setTimeout(() => {
        button.onclick = null;
        display.textContent = 'Игра Завершена';

        clearInterval(interval);
        clearTimeout(timeout);
    }, TIMEOUT);
}
/*функция для преобразования миллисекунд в секунды с 2мя знаками после запятой!
(пр. 3500 мс станут 3.50) */
function formatTime(ms) {
    return Number.parseFloat(ms / 1000).toFixed(2);
}