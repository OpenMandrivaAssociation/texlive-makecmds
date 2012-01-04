# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/makecmds
# catalog-date 2009-09-03 08:40:46 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-makecmds
Version:	20090903
Release:	2
Summary:	The new \makecommand command always (re)defines a command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/makecmds
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecmds.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecmds.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makecmds.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a \makecommand command, which is like
\(re)newcommand except it always (re)defines a command. There
is also \makeenvironment and \provideenvironment for
environments.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/makecmds/makecmds.sty
%doc %{_texmfdistdir}/doc/latex/makecmds/README
%doc %{_texmfdistdir}/doc/latex/makecmds/makecmds.pdf
#- source
%doc %{_texmfdistdir}/source/latex/makecmds/makecmds.dtx
%doc %{_texmfdistdir}/source/latex/makecmds/makecmds.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
