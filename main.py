from thinkgear import ThinkGearProtocol, ThinkGearAttentionData, ThinkGearMeditationData, ThinkGearRawWaveData
import time

tg = ThinkGearProtocol('/dev/rfcomm0')

for pkt in tg.get_packets():
	for d in pkt:
		#print isinstance(d, ThinkGearAttentionData)
		#print "-------------"
		if isinstance(d, ThinkGearAttentionData):
			print "attention:", d.value
		if isinstance(d, ThinkGearMeditationData):
			print "meditation:", d.value
		# if isinstance(d, ThinkGearRawWaveData):
		# 	print "Raw:", d.value