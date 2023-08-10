_A=False
import os,sys,yaml,python_minifier
from localstack_obfuscator.ls_patches import patch
CONFIG_FILE_NAME='obfuscator.yml'
def root_code_dir():dir=os.path.dirname(os.path.realpath(__file__));return os.path.realpath(os.path.join(dir,''))
def mkdir(path):
	if not os.path.exists(path):os.makedirs(path)
def run(cmd):os.system(cmd)
def copy_target_code(target_dir,output_dir_name):B=target_dir;A=os.path.realpath(os.path.join(B,'..',output_dir_name));mkdir(A);C='cp -r "%s" "%s/"'%(B,A);print(f"Copying target code to {A}");run(C);return A
def apply_python_minifier_patches():
	'Idempotent operation that applies required patches to python-minifier';C=True;import ast as B;from python_minifier.transforms.remove_annotations import RemoveAnnotations as A
	def F(node):
		E='dataclasses';D='dataclass';A=node
		if not isinstance(A.parent,B.ClassDef):return _A
		if len(A.parent.decorator_list)==0:return _A
		for A in A.parent.decorator_list:
			if isinstance(A,B.Name)and A.id==D:return C
			elif isinstance(A,B.Call)and isinstance(A.func,B.Name)and A.func.id==D:return C
			elif isinstance(A,B.Attribute)and A.attr==D and A.value.id==E:return C
			elif isinstance(A,B.Call)and isinstance(A.func,B.Attribute)and A.func.attr==D and A.func.value.id==E:return C
		return _A
	if not hasattr(A.visit_AnnAssign,'_ls_patched'):
		@patch(A.visit_AnnAssign)
		def D(fn,self,node):
			E='annotation';A=node
			if F(A):return A
			if isinstance(A,B.AnnAssign):
				D=getattr(A,E,None);C=fn(self,A);G=getattr(C,E,None)
				if isinstance(G,B.Constant)and isinstance(D,(B.Subscript,B.Name)):C.annotation=D
				return C
			return fn(self,A)
		A.visit_AnnAssign._ls_patched=C
def load_file(path):
	with open(path,'r')as A:return A.read()
def save_file(path,content):
	with open(path,'w')as A:return A.write(content)
def load_config(target):
	A=os.path.join(target,CONFIG_FILE_NAME)
	try:B=open(A,'r');return yaml.safe_load(B)
	except FileNotFoundError:print(f"No {CONFIG_FILE_NAME} file found in target directory");return{}
def obfuscate(dirpath):
	G='target_dir';A=dirpath;A=os.path.realpath(A);B=load_config(A)
	if B.get('custom_patches',_A):apply_python_minifier_patches()
	if B.get(G):D=os.path.join(A,B.get(G))
	else:H=os.path.basename(A);D=os.path.join(A,H)
	E=copy_target_code(D,B.get('output_dir','build'));I=B.get('minify',{});J=B.get('exclude',[]);print(f"Obfuscating code in {E}")
	for(K,N,L)in os.walk(os.path.join(E)):
		for C in L:
			if C in J or not C.endswith('.py'):continue
			F=os.path.join(K,C);M=python_minifier.minify(load_file(F),**I);save_file(F,M)
	print('Done!')
def main():
	A=sys.argv[1:]
	if len(A)!=1:print('Usage: localstack-obfuscator <dirpath>');sys.exit(1)
	B=A[0];obfuscate(B)
if __name__=='__main__':main()