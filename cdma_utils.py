def XORing(c, d):
    return [di ^ ci for di in d for ci in c]

def convertBitToSignal(arr):
    return [1 if x == 0 else -1 for x in arr]

def chain_encode(c1, c2, c3, d1, d2, d3):
    s1 = convertBitToSignal(XORing(c1, d1))
    s2 = convertBitToSignal(XORing(c2, d2))
    s3 = convertBitToSignal(XORing(c3, d3))

    signal = [s1[i] + s2[i] + s3[i] for i in range(len(s1))]
    return signal

def decode(signal, bits):
    bits = convertBitToSignal(bits)
    L = len(bits)

    data_len = len(signal) // L
    decoded = []

    for i in range(data_len):
        chunk = signal[i*L:(i+1)*L]
        res = sum(chunk[k] * bits[k] for k in range(L))
        decoded.append(0 if res > 0 else 1)

    return decoded
