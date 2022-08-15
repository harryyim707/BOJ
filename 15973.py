p = list(map(int, input().split()))
q = list(map(int, input().split()))
px = p[2]-p[0]
py = p[3]-p[1]
qx = q[2]-q[0]
qy = q[3]-q[1]
pc = [p[0]+px/2, p[1]+py/2]
qc = [q[0]+qx/2, q[1]+qy/2]

if abs(pc[0] - qc[0]) == px/2+qx/2 and abs(pc[1]-qc[1]) == py/2 + qy/2:
    print("POINT")
elif (abs(pc[0] - qc[0]) == px/2+qx/2 and abs(pc[1]-qc[1]) < py/2 + qy/2) or (abs(pc[0]-qc[0]) < px/2 + qx/2 and abs(pc[1]-qc[1]) == py/2 + qy/2):
    print("LINE")
elif abs(qc[0]-pc[0]) < (px+qx)/2 and abs(qc[1]-pc[1]) < (py+qy)/2:
    print("FACE")
else:
    print("NULL")