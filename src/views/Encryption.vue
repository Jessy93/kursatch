<template>
    <div class="col s12 m6 l2 card">
        <div class="card-content light-blue white-text">
            <div class="card-title">
                Шифрование и Дешифрование
            </div>

            <p>
                В этом разделе рассказывается о прототипе шифрования и дешифрования ваших файлов.
                <br/><br/>
                Чтобы протестировать пример:
                <br/>- Нажмите кнопку «плюс»
                <br/>- Затем выберите файл для шифрования
                <br/>- Введите пароль шифрования. (пароль по умолчанию 0000 или пароль пользователя).
            </p>
            <DeviceSidebar />
        </div>
    </div>
</template>

<script>
import DeviceSidebar from '@/components/Encryption/DeviceSidebar'

export default {
  name: "Encryption",
  components:  { DeviceSidebar },
};
</script>
