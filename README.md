HiggsAnalysis-CombinedLimit
===========================

### Official documentation

[Manual to run combine](http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/)

### Standalone compilation in `lxplus`
```
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
source env_standalone.sh
make -j 8; make # second make fixes compilation error of first
```

### To Collaborate with a colleague's fork

If I want to pull from Chris's code:

```
git remote add cawest-HiggsAnalysis https://github.com/christopheralanwest/HiggsAnalysis-CombinedLimit/
git checkout -b cawest_ADD-102x
git pull cawest-HiggsAnalysis ADD-102x
git push origin cawest_ADD-102x
source env_standalone.sh
make -j 8
```
