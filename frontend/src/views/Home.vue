<template>
    <div class="m-auto w-3/4" style="display: flex;flex-direction:column;">
        <vue3-chart-js
            :id="lineChart.id"
            :type="lineChart.type"
            :data="lineChart.data"
            :options="lineChart.options"
            ref="chartRef"
        ></vue3-chart-js>
    </div>

    <div class="mt-4 px-2 py-4 w-full text-center">
        <input style="width: 550px" class="m-auto border-2 rounded-md px-2 py-1" v-model.trim="stockNumber" v-on:keyup.enter="sent" placeholder="請輸入欲查詢的股票代號（如 2330, 0050, 0056）" />
        <div class="m-2">
            <button class="hover:bg-blue-700 bg-blue-500 rounded-sm font-bold px-2 py-1 text-white" @click="sent">送出</button>
        </div>
    </div>
</template>

<script>
import shared from "@/share/shared"
import {ref, reactive} from "vue"
import axios from 'axios'
import {Decimal} from 'decimal.js'
import Vue3ChartJs from '@j-t-mcc/vue3-chartjs'
// import zoomPlugin from 'chartjs-plugin-zoom'

// Vue3ChartJs.registerGlobalPlugins([zoomPlugin])

let apiBaseURL = shared.getAPIBaseURL()

export default {
    name: 'Home',
    components: {
        Vue3ChartJs,
      },
    setup() {
        let stockNumber = ref(null)
        let chartRef = ref(null)

        const calculateAveragePrice = function(price, days) {
            let result = []
            let sum = price[0].mul(new Decimal(days))
            result[0] = sum.div(new Decimal(days)).toNumber()
            for (let i = 1; i < price.length; ++i) {
                sum = sum.add(price[i]).sub(price[Math.max(0, i - days)])
                result[i] = sum.div(new Decimal(days)).toNumber()
            }
            return result
        }

        const sent = async function() {
            lineChart.options.plugins.title.text = stockNumber.value + " Closing Price"
            try {
                let result = await axios.get(apiBaseURL + "/" + stockNumber.value)
                let price = []
                for (let i = 0; i < result.data.length; ++i) price[i] = new Decimal(Number(result.data[i].price))
                for (let i = 0; i < result.data.length; ++i) lineChart.data.labels[i] = result.data[i].date

                let length = price.length
                let scale = 50

                lineChart.data.datasets[0].data = calculateAveragePrice(price, 1).slice(length - scale, length)
                lineChart.data.datasets[1].data = calculateAveragePrice(price, 5).slice(length - scale, length)
                lineChart.data.datasets[2].data = calculateAveragePrice(price, 20).slice(length - scale, length)
                lineChart.data.labels = lineChart.data.labels.slice(length - scale, length)
            } catch (error) {
                if (error.response) {
                    let statusCode = error.response.status
                    console.log(statusCode)
                    if (statusCode == 404) {
                        alert("目前尚未支援該股票")
                    }
                }
            }
            console.log("hi")
            chartRef.value.update(500)
        }

        const lineChart = reactive({
            id: 'line',
            type: 'line',
            data: {
                labels: [],
                datasets: [
                    {
                        label: "每日收盤價",
                        backgroundColor: [
                            'rgba(151,187,205,1)',
                        ],
                        strokeColor: "rgba(151,187,205,1)",
                        pointColor: "rgba(151,187,205,1)",
                        pointStrokeColor: "#fff",
                        pointHighlightFill: "#fff",
                        pointHighlightStroke: "rgba(151,187,205,1)",
                        data: []
                    },
                    {
                        label: "五日收盤價",
                        backgroundColor: [
                            'rgba(245, 15, 15, 0.5)',
                        ],
                        strokeColor: "rgba(245, 15, 15, 0.5)",
                        pointColor: "rgba(245, 15, 15, 0.5)",
                        pointStrokeColor: "#fff",
                        pointHighlightFill: "#fff",
                        pointHighlightStroke: "rgba(245, 15, 15, 0.5)",
                        data: []
                    },
                    {
                        label: "二十日收盤價",
                        backgroundColor: [
                            'rgba(41, 181, 47, 1)',
                        ],
                        strokeColor: "rgba(41, 181, 47, 1)",
                        pointColor: "rgba(41, 181, 47, 1)",
                        pointStrokeColor: "#fff",
                        pointHighlightFill: "#fff",
                        pointHighlightStroke: "rgba(41, 181, 47, 1)",
                        data: []
                    }
                ]
            },
            options: {
                plugins: {
                    title: {
                        display: true,
                        text: "Closing Price"
                    },

                }
            }
        })

        return {sent, stockNumber, lineChart, chartRef}
    }
}

</script>

<style>
</style>
