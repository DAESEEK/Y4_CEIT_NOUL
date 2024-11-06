import React, { useState, useEffect } from 'react'
import {
    View,
    Text,
    Button,
    Alert,
    FlatList,
    StyleSheet,
    TouchableOpacity,
} from 'react-native'

const SERVER_URL = 'http://127.0.0.1:5000' // Flask 서버 URL

const App = () => {
    const [logs, setLogs] = useState([])

    // LED 제어 함수
    const controlLED = async (color, action) => {
        try {
            const response = await fetch(`${SERVER_URL}/led`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ color, action }),
            })

            if (response.ok) {
                Alert.alert(
                    'LED Control',
                    `${color.toUpperCase()} LED ${action.toUpperCase()} command sent.`
                )
                fetchLogs() // 명령어 전송 후 로그 갱신
            } else {
                Alert.alert('Error', 'Failed to send LED command.')
            }
        } catch (error) {
            console.error(error)
            Alert.alert(
                'Error',
                'An error occurred while sending the LED command.'
            )
        }
    }

    // LED 조작 기록 조회 함수
    const fetchLogs = async () => {
        try {
            const response = await fetch(`${SERVER_URL}/led_log`)
            const data = await response.json()
            setLogs(data)
        } catch (error) {
            console.error(error)
            Alert.alert('Error', 'An error occurred while fetching logs.')
        }
    }

    // 페이지 로드 시 초기 로그 조회
    useEffect(() => {
        fetchLogs()
    }, [])

    // 로그 항목 렌더링 함수
    const renderLog = ({ item }) => (
        <View style={styles.logEntry}>
            <Text>{`${
                item.timestamp
            } - ${item.color.toUpperCase()} LED ${item.action.toUpperCase()}`}</Text>
        </View>
    )

    return (
        <View style={styles.container}>
            <Text style={styles.title}>LED Control App</Text>
            <View style={styles.buttonGroup}>
                <TouchableOpacity
                    style={[styles.button, styles.red]}
                    onPress={() => controlLED('red', 'on')}
                >
                    <Text style={styles.buttonText}>Red ON</Text>
                </TouchableOpacity>
                <TouchableOpacity
                    style={[styles.button, styles.red]}
                    onPress={() => controlLED('red', 'off')}
                >
                    <Text style={styles.buttonText}>Red OFF</Text>
                </TouchableOpacity>
                <TouchableOpacity
                    style={[styles.button, styles.green]}
                    onPress={() => controlLED('green', 'on')}
                >
                    <Text style={styles.buttonText}>Green ON</Text>
                </TouchableOpacity>
                <TouchableOpacity
                    style={[styles.button, styles.green]}
                    onPress={() => controlLED('green', 'off')}
                >
                    <Text style={styles.buttonText}>Green OFF</Text>
                </TouchableOpacity>
                <TouchableOpacity
                    style={[styles.button, styles.blue]}
                    onPress={() => controlLED('blue', 'on')}
                >
                    <Text style={styles.buttonText}>Blue ON</Text>
                </TouchableOpacity>
                <TouchableOpacity
                    style={[styles.button, styles.blue]}
                    onPress={() => controlLED('blue', 'off')}
                >
                    <Text style={styles.buttonText}>Blue OFF</Text>
                </TouchableOpacity>
            </View>
            <Text style={styles.logTitle}>LED Control Logs</Text>
            <FlatList
                data={logs}
                renderItem={renderLog}
                keyExtractor={(item, index) => index.toString()}
                style={styles.logContainer}
            />
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        padding: 20,
        backgroundColor: '#f4f4f4',
    },
    title: {
        fontSize: 24,
        fontWeight: 'bold',
        marginVertical: 20,
    },
    buttonGroup: {
        flexDirection: 'row',
        flexWrap: 'wrap',
        justifyContent: 'center',
        marginBottom: 20,
    },
    button: {
        width: '40%',
        margin: 10,
        paddingVertical: 10,
        borderRadius: 8,
        alignItems: 'center',
    },
    buttonText: {
        color: 'white',
        fontSize: 16,
        fontWeight: 'bold',
    },
    red: { backgroundColor: '#ff4c4c' },
    green: { backgroundColor: '#32cd32' },
    blue: { backgroundColor: '#4c6cff' },
    logTitle: {
        fontSize: 20,
        fontWeight: 'bold',
        marginBottom: 10,
    },
    logContainer: {
        width: '100%',
    },
    logEntry: {
        padding: 10,
        backgroundColor: '#ffffff',
        borderBottomWidth: 1,
        borderColor: '#cccccc',
    },
})

export default App
