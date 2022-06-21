<template>
    <div class="text-center text-4xl">Stock closing price visualizer</div>
    <div class="mt-4 px-2 py-4 w-full text-center">
        <input style="width: 600px" class="m-auto border-2 p-1" placeholder="請輸入欲查詢的股票代號（如 2330, 0050, 0056）" />
        <div class="m-2">
            <button class="hover:bg-blue-700 bg-blue-500 px-2 py-1 text-white" @click="sent">送出</button>
        </div>
    </div>
</template>

<script>
import shared from "@/share/shared"
export default {
    name: 'Home',
    setup() {
        const sent = function() {
            alert(shared.getAPIBaseURL())
        }
        return {sent}
    }
}


</script>

<style>
</style>
