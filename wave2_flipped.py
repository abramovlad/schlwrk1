import wave, struct

source = wave.open("in.wav", mode='rb')
dest = wave.open("out.wav", mode='wb')
dest.setparams(source.getparams())
fr_count = source.getnframes()
data = struct.unpack('<' + str(fr_count) + 'h', source.readframes(fr_count))
newdata = data[::-1]
newframes = struct.pack('<' + str(len(newdata)) + 'h', *newdata)
dest.writeframes(newframes)
source.close()
dest.close()
